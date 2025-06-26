import streamlit as st

#  this is the correct file

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def cl_col():
    st.rerun()


if 'counter_A' not in st.session_state:
    st.session_state['counter_A'] = 0

if 'counter_B' not in st.session_state:
    st.session_state['counter_B'] = 0


st.markdown("""
<style>
    .stApp {
        background-color: green;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('''
    <div style='text-align: center'>
        <h2 style='display: inline-block; padding-bottom: 5px'>INCOME CALCULATOR</h2>
    </div>
    ''', unsafe_allow_html=True)
st.write(" ")

col1, col2 = st.columns([2, 2])

with (col1):
    st.markdown("""<h3 style="text-align: center; color: "white"; >Hourly Rate Calculations</h3""",
                unsafe_allow_html=True)
    H_text = st.text_input(" ", placeholder="Enter hourly rate...", key="hour")
    if st.button("Calculate", key="--H_CALC--"):
        H_inner_col1, H_inner_col2 = st.columns(2)
        with H_inner_col1:
            try:
                fl_annual = float(st.session_state.hour)
                GST = 0.10
                A_hourly = fl_annual * 7.6 * 5 * 4 * 12
                A_monthly = fl_annual * 7.6 * 5 * 4
                A_weekly = fl_annual * 7.6 * 5
                A_GST_annually = A_hourly * GST
                A_GST_monthly = A_monthly * GST
                A_GST_weekly = A_weekly * GST
                st.markdown("<strong>GROSS</strong>", unsafe_allow_html=True)
                if is_number(fl_annual):
                    st.write(f"Annually: <strong style='padding:7px; color:black;'>${A_hourly:,.2f}</strong>", unsafe_allow_html=True)
                    st.write(f"Monthly: <strong style='padding:10px; color:black;'>${A_monthly:,.2f}</strong>", unsafe_allow_html=True)
                    st.write(f"Weekly: <strong style='padding:15px; color:black;'>${A_weekly:,.2f}</strong>", unsafe_allow_html=True)
                    with H_inner_col2:
                        st.markdown("<strong>NET</strong>", unsafe_allow_html=True)
                        if is_number(fl_annual):
                            st.write(f"Annually: <strong style='padding:7px; color:black;'>${A_hourly - A_GST_annually:,.2f}</strong>",
                                     unsafe_allow_html=True)
                            st.write(f"Monthly: <strong style='padding:10px; color:black;'>${A_monthly - A_GST_monthly:,.2f}</strong>",
                                     unsafe_allow_html=True)
                            st.write(f"Weekly: <strong style='padding:15px; color:black;'>${A_weekly - A_GST_weekly:,.2f}</strong>",
                                     unsafe_allow_html=True)
            except ValueError:
                  st.write("Ensure only numbers are entered.")
    if st.button("Clear", key="--CL_COL1--"):
        st.session_state.counter_A += 1

with (col2):
    st.markdown("""<h3 style="text-align: center; color: "white"; >Annual Rate Calculations</h3""",
                unsafe_allow_html=True)
    A_input = st.text_input("Enter hourly rate...", key="annual")
    if st.button("Calculate", key="--A_CALC--"):
        A_inner_col1, A_inner_col2 = st.columns(2)
        with A_inner_col1:
            try:
                fl_annual = float(st.session_state.annual)
                GST = 0.10
                A_monthly = fl_annual / 12
                A_weekly = fl_annual / 12 / 4
                A_hourly = fl_annual / 12 / 4 / 5 / 7.6
                A_GST_monthly = A_monthly * GST
                A_GST_weekly = A_weekly * GST
                A_GST_hourly = A_hourly * GST
                st.markdown("<strong>GROSS</strong>", unsafe_allow_html=True)
                if is_number(fl_annual):
                    st.write(f"Monthly: <strong style='padding:10px; color:black;'>${A_monthly:,.2f}</strong>", unsafe_allow_html=True)
                    st.write(f"Weekly: <strong style='padding:18px; color:black;'>${A_weekly:,.2f}</strong>", unsafe_allow_html=True)
                    st.write(f"Hourly: <strong style='padding:20px; color:black;'>${A_hourly:,.2f}</strong>", unsafe_allow_html=True)
                    with A_inner_col2:
                        st.markdown("<strong>NET</strong>", unsafe_allow_html=True)
                        if is_number(fl_annual):
                            st.write(f"Monthly: <strong style='padding:10px; color:black;'>${A_monthly - A_GST_monthly:,.2f}</strong>",
                                     unsafe_allow_html=True)
                            st.write(f"Weekly: <strong style='padding:18px; color:black;'>${A_weekly - A_GST_weekly:,.2f}</strong>",
                                     unsafe_allow_html=True)
                            st.write(f"Hourly: <strong style='padding:20px; color:black;'>${A_hourly - A_GST_hourly:,.2f}</strong>",
                                     unsafe_allow_html=True)
            except ValueError:
                  st.write("Ensure only numbers are entered.")
    if st.button("Clear", key="--CL_COL2--"):
        st.session_state.counter_B += 1

print(st.session_state.counter_A)
print(st.session_state.counter_B)










