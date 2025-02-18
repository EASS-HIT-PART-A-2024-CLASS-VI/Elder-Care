import streamlit as st
from api_client import fetch_data, add_data, delete_data, update_task_status

def manage_elderly():
    st.subheader("👴 Manage Elderly")

    
    st.markdown(
        """
        <style>
        div[data-testid="stExpander"] {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 8px;
            margin-bottom: 6px;
            background-color: #f9f9f9;
            transition: all 0.3s ease-in-out;
        }

        div[data-testid="stExpander"]:hover {
            background-color: #e9f5ff;
            border: 1px solid #4fdee3;
        }

        .expander-title {
            font-size: 16px;
            font-weight: bold;
            color: #333;
            display: flex;
            align-items: center;
        }

        .icon {
            margin-right: 8px;
            font-size: 18px;
        }

        .highlighted {
            color: red;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    try:
        elderly_data = fetch_data("elderly")
        caregiver_data = fetch_data("caregivers")

        for elderly in elderly_data:
            # If the elderly person has a caregiver - the icon changes
            icon = "❤️" if elderly.get("assignments") else "🧑‍🦳"

            # If there are many tasks the name is highlighted
            name_class = "highlighted" if len(elderly.get("tasks", [])) > 3 else ""

            
            expander_label = f"{icon} {elderly['name']} (ID: {elderly['id']})"

            with st.expander(expander_label, expanded=False):
                col1, col2 = st.columns([8, 2])
                with col1:
                    st.markdown(f"### 👴 **{elderly['name']}**")
                    st.markdown(f"🔢 **ID:** {elderly['id']}")
                with col2:
                    if st.button(f"❌ Delete", key=f"delete_elderly_{elderly['id']}"):
                        delete_data(f"elderly/{elderly['id']}")
                        st.success(f"Elderly {elderly['name']} deleted successfully!")
                        continue  

                
                tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["✅ Tasks", "💊 Medications", "➕ Add Task", "➕ Add Medication", "👨‍⚕️ Assign Caregiver", "🚫 Unassign Caregiver"])

                
                with tab1:
                    st.markdown("#### ✅ Tasks:")
                    if elderly.get("tasks"):
                        for task in elderly["tasks"]:
                            task_status = "🟢" if task['status'] == "complete" else "🔴"
                            st.markdown(f"{task_status} **{task['description']}** *(Status: {task['status']})*")

                            new_status = st.text_input(f"Update Status for Task {task['id']}", value=task['status'], key=f"update_status_{task['id']}")
                            if st.button(f"Update Task {task['id']} Status", key=f"update_task_status_{task['id']}"):
                                update_task_status(elderly['id'], task['id'], new_status)
                                st.success(f"Task {task['id']} status updated!")

                            if st.button(f"❌ Delete Task {task['id']}", key=f"delete_task_{task['id']}"):
                                delete_data(f"elderly/{elderly['id']}/tasks/{task['id']}")
                                st.success(f"Task {task['id']} deleted!")

                    else:
                        st.info("No tasks assigned.")

                
                with tab2:
                    st.markdown("#### 💊 Medications:")
                    if elderly.get("medications"):
                        meds_data = [{"Medication": med["name"], "Dosage": med["dosage"], "Frequency": med["frequency"]}
                                     for med in elderly["medications"]]
                        st.table(meds_data)
                    else:
                        st.warning("No medications assigned.")

                
                with tab3:
                    description = st.text_input(f"Task Description for {elderly['name']}", key=f"task_description_{elderly['id']}")
                    status = st.text_input("Task Status", value="pending", key=f"task_status_{elderly['id']}")
                    if st.button(f"➕ Add Task", key=f"add_task_{elderly['id']}"):
                        payload = {"description": description, "status": status}
                        add_data(f"elderly/{elderly['id']}/tasks", payload)
                        st.success(f"Task added successfully!")

                
                with tab4:
                    name = st.text_input(f"Medication Name for {elderly['name']}", key=f"medication_name_{elderly['id']}")
                    dosage = st.text_input(f"Dosage", key=f"medication_dosage_{elderly['id']}")
                    frequency = st.text_input(f"Frequency", key=f"medication_frequency_{elderly['id']}")
                    if st.button(f"➕ Add Medication", key=f"add_medication_{elderly['id']}"):
                        payload = {"name": name, "dosage": dosage, "frequency": frequency}
                        add_data(f"elderly/{elderly['id']}/medications", payload)
                        st.success(f"Medication {name} added successfully!")

               
                with tab5:
                    st.markdown("#### 👨‍⚕️ Assign Caregiver:")
                    caregiver_options = {caregiver['id']: f"{caregiver['name']} (ID: {caregiver['id']})" for caregiver in caregiver_data}
                    selected_caregiver_id = st.selectbox("Select Caregiver", options=list(caregiver_options.keys()), format_func=lambda x: caregiver_options[x], key=f"select_caregiver_{elderly['id']}")
                    if st.button(f"Assign Caregiver", key=f"assign_caregiver_{elderly['id']}"):
                        payload = {"caregiver_id": selected_caregiver_id, "elderly_id": elderly['id']}
                        add_data("caregiver-assignments", payload)
                        st.success(f"Caregiver assigned successfully!")

                
                with tab6:
                    st.markdown("#### 🚫 Unassign Caregiver:")
                    if elderly.get("assignments"):
                        for assignment in elderly["assignments"]:
                            caregiver_info = fetch_data(f"caregivers/{assignment['caregiver_id']}")
                            col1, col2 = st.columns([8, 2])
                            with col1:
                                st.write(f"- {caregiver_info['name']} (ID: {caregiver_info['id']})")
                            with col2:
                                if st.button(f"🚫 Unassign {caregiver_info['name']}", key=f"delete_assignment_{assignment['id']}"):
                                    delete_data(f"caregiver-assignments/{assignment['id']}")
                                    st.success(f"Caregiver {caregiver_info['name']} removed!")
                    else:
                        st.warning("No caregivers assigned.")

    except RuntimeError as e:
        st.error(str(e))
