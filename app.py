import streamlit as st

# 1. ページ基本設定
st.set_page_config(page_title="Fanspot 見積エージェント", layout="wide")
st.title("🎯 Fanspot 案件見積エージェント")

# 2. サイドバーに入力項目
st.sidebar.header("📋 条件入力")
period = st.sidebar.number_input("施策期間 (月数)", min_value=1, value=2)
winners = st.sidebar.number_input("当選者数", min_value=0, value=10000, step=1000)
is_iw = st.sidebar.radio("インスタントウィン", ["有り", "無し"])
update = st.sidebar.number_input("ページ更新回数", min_value=0, value=1)

# 💡 設定値の定義（ここで一括管理することで可視化と計算を同期させます）
CONFIG = {
    "fanspot_init": 3500000,
    "receipt_impl": 1000000,
    "iw_impl": 3000000,
    "monthly_fee": 650000,
    "jimukyoku_fee": 400000,
    "update_fee": 1000000,
    "lottery_fee": 50000,
    "meken_unit_price": 1000,
    "meken_ratio": 2  # 当選者数の2倍
}

# 3. 見積算出ロジック
if st.sidebar.button("🚀 見積もりを算出"):
    # 事務局と目検のロジック計算
    j_months = period + 1
    m_count = winners * CONFIG["meken_ratio"]
    m_cost = m_count * CONFIG["meken_unit_price"]
    
    iw_cost = CONFIG["iw_impl"] if is_iw == "有り" else 0
    
    # 合計計算
    init_costs = CONFIG["fanspot_init"] + CONFIG["receipt_impl"] + iw_cost + m_cost + CONFIG["lottery_fee"]
    oper_costs = (CONFIG["monthly_fee"] * period) + (CONFIG["jimukyoku_fee"] * j_months) + (CONFIG["update_fee"] * update)
    total_cost = init_costs
