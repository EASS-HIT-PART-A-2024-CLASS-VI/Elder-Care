import streamlit as st
from api_client import fetch_data

def view_data():
    st.subheader("📊 Elderly & Caregivers Overview")
    data_type = st.selectbox("Choose profile type", ["Elderly", "Caregivers"])

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

        .expander-title .icon {
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

    if st.button("Show information"):
        try:
            data = fetch_data(data_type.lower())

            if data_type == "Elderly":
                st.write("### 🏡 Elderly List:")
                for entry in data:
                    # Determining an icon according to whether there is a caregiver 
                    icon = "❤️" if entry.get("assignments") else "🧑‍🦳"
                    
                    
                    expander_label = f"{entry['name']} (ID: {entry['id']})"

                    with st.expander(expander_label, expanded=False):
                        st.markdown(f"### {icon} **{entry['name']}**")
                        st.markdown(f"🔢 **ID:** {entry['id']}")

                        #Tasks presentation
                        st.markdown("#### ✅ Tasks:")
                        if entry.get("tasks"):
                            for task in entry["tasks"]:
                                task_status = "🟢" if task['status'] == "complete" else "🔴"
                                st.markdown(f"{task_status} **{task['description']}** *(Status: {task['status']})*")
                        else:
                            st.info("No tasks assigned.")

                        # Medication presentation
                        st.markdown("#### 💊 Medications:")
                        if entry.get("medications"):
                            meds_data = [{"Medication": med["name"], "Dosage": med["dosage"], "Frequency": med["frequency"]}
                                         for med in entry["medications"]]
                            st.table(meds_data)
                        else:
                            st.warning("No medications assigned.")

                        #Caregivers related to specific elder presentation
                        st.markdown("#### 👨‍⚕️ Caregivers:")
                        if entry.get("assignments"):
                            for assignment in entry["assignments"]:
                                caregiver_info = fetch_data(f"caregivers/{assignment['caregiver_id']}")
                                st.success(f"👨‍⚕️ {caregiver_info['name']} (ID: {caregiver_info['id']})")
                        else:
                            st.error("No caregivers assigned.")

            elif data_type == "Caregivers":
                st.write("### 🏥 Caregivers List:")
                for caregiver in data:
                    expander_label = f"{caregiver['name']} (ID: {caregiver['id']})"

                    with st.expander(expander_label, expanded=False):
                        st.markdown(f"### 👨‍⚕️ Name: **{caregiver['name']}**")
                        st.markdown(f"🔢 **ID:** {caregiver['id']}")

                        st.markdown("#### 🏦 Bank Details:")
                        st.markdown(f"- **Bank Name:** {caregiver.get('bank_name', 'N/A')}")
                        st.markdown(f"- **Bank Account:** {caregiver.get('bank_account', 'N/A')}")
                        st.markdown(f"- **Branch Number:** {caregiver.get('branch_number', 'N/A')}")

                        # 🏡 Elderly related to specific caregiver presentation
                        st.markdown("#### 👴 Assigned Elderly:")
                        if caregiver.get("assignments"):
                            for assignment in caregiver["assignments"]:
                                elderly_info = fetch_data(f"elderly/{assignment['elderly_id']}")
                                st.success(f"👴 {elderly_info['name']} (ID: {elderly_info['id']})")
                        else:
                            st.info("No elderly individuals assigned.")

                       
                        st.markdown("#### 💰 Salary Details:")
                        salary_data = caregiver.get('salary', {})
                        st.markdown(f"- **Base Salary:** {salary_data.get('price', 'N/A')}")
                        st.markdown(f"- **Amount:** {salary_data.get('amount', 'N/A')}")
                        st.markdown(f"- **Total:** {salary_data.get('total', 'N/A')}")

                       
                        saturday_data = caregiver.get('saturday', {})
                        st.markdown("#### 🏖️ Saturday Pay:")
                        st.markdown(f"- **Base:** {saturday_data.get('price', 'N/A')}")
                        st.markdown(f"- **Amount:** {saturday_data.get('amount', 'N/A')}")
                        st.markdown(f"- **Total:** {saturday_data.get('total', 'N/A')}")

                        
                        allowance_data = caregiver.get('allowance', {})
                        st.markdown("#### 🎁 Allowance:")
                        st.markdown(f"- **Base:** {allowance_data.get('price', 'N/A')}")
                        st.markdown(f"- **Amount:** {allowance_data.get('amount', 'N/A')}")
                        st.markdown(f"- **Total:** {allowance_data.get('total', 'N/A')}")

                       
                        total_bank = caregiver.get('total_bank', 'N/A')
                        st.markdown(f"#### 🏦 **Total Bank Balance:** {total_bank}")

        except RuntimeError as e:
            st.error(str(e))       