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

# 3. 見積算出ロジック
if st.sidebar.button("🚀 見積もりを算出"):
    # ロジック計算
    j_months = period + 1
    m_count = winners * 2
    m_cost = m_count * 1000
    iw_cost = 3000000 if is_iw == "有り" else 0
    
    # 費用合計
    init_costs = 3500000 + 1000000 + iw_cost + m_cost + 50000
    oper_costs = (650000 * period) + (400000 * j_months) + (1000000 * update)
    total_cost = init_costs + oper_costs

    # 4. 画面表示：見積結果
    st.header(f"合計費用（税抜）: {total_cost:,}円")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### **■ 初期費用: {init_costs:,}円**")
        st.write(f"・Fanspot初期設定/実装: 4,500,000円")
        st.write(f"・FanSpot インスタントウィン実装: {iw_cost:,}円")
        st.write(f"・目検作業費用 ({m_count:,}枚): {m_cost:,}円")
        st.write(f"・抽選費用: 50,000円")
    with col2:
        st.markdown(f"### **■ 運用費用: {oper_costs:,}円**")
        st.write(f"・Fanspot 月額費用 ({period}ヶ月): {650000*period:,}円")
        st.write(f"・問合せ事務局対応 ({j_months}ヶ月): {400000*j_months:,}円")
        st.write(f"・FanSpot ページ更新費 ({update}回): {1000000*update:,}円")
    
    st.divider()
    
    # 5. 💡 【詳細版】算出ロジックの根拠
    st.markdown("### 🔍
