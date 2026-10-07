import streamlit as st
from starter import ZONES, TIME_BLOCKS, COSTS, delivery_times


# 1. Reuse the notebook's best-promise calculation.
def best_promise(zone, time_block, promises, costs):
    best_promise_time = None
    best_net_profit = None

    for promise in promises:
        times = delivery_times(zone, time_block, promise, seed=1)
        all_orders = len(times)
        late_orders = sum(times > promise)

        profit = all_orders * costs['margin']
        cst = (
            late_orders * costs['refund']
            + late_orders * costs['churn_orders'] * costs['margin']
        )
        net_profit = profit - cst

        if best_net_profit is None or net_profit > best_net_profit:
            best_net_profit = net_profit
            best_promise_time = promise

    return best_promise_time, round(float(best_net_profit), 2)


# 2. Introduce the app and select the delivery scenario.
st.title("Rosa's Delivery Promise")
st.write("Find the promise time with the highest net profit for a zone and time block.")

zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)


# 3. Choose an inclusive promise range in 5-minute steps.
st.subheader("Promise range")
min_promise = st.number_input(
    "Minimum promise (minutes)", min_value=5, value=5, step=5
)
max_promise = st.number_input(
    "Maximum promise (minutes)", min_value=5, value=90, step=5
)
st.caption("Both endpoints are included. Promises are tested every 5 minutes.")


# 4. Set costs using the notebook's default values and units.
st.subheader("Costs and profit")
refund = st.number_input(
    "Refund cost per late order ($)",
    min_value=0.0,
    value=float(COSTS['refund']),
    step=0.5,
)
churn = st.number_input(
    "Churn per late order (future orders lost)",
    min_value=0.0,
    value=float(COSTS['churn_orders']),
    step=0.1,
)
margin = st.number_input(
    "Profit margin per order ($)",
    min_value=0.0,
    value=float(COSTS['margin']),
    step=0.5,
)

costs = {'refund': refund, 'churn_orders': churn, 'margin': margin}


# 5. Validate the range and display the result when the button is clicked.
if st.button("Calculate recommended promise"):
    if min_promise > max_promise:
        st.error("The minimum promise must be no greater than the maximum promise.")
    elif min_promise % 5 != 0 or max_promise % 5 != 0:
        st.error("Enter promise times that are multiples of 5 minutes.")
    else:
        promises = list(range(min_promise, max_promise + 1, 5))
        recommended_promise, net_profit = best_promise(
            zone, time_block, promises, costs
        )

        st.metric("Recommended promise", f"{recommended_promise} minutes")
        st.metric("Net profit (four simulated weeks)", f"${net_profit:,.2f}")
