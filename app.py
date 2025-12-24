import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="マストバイCP見積もりエージェント", layout="wide")
st.title("🎯 マストバイCP見積もりエージェント")

# 2. 条件入力
st.sidebar.header("📋 条件入力")
period = st.sidebar.number_input("施策期間 (月数)", min_value=1, value=2)
winners = st.sidebar.number_input("当選者数", min_value=0, value=10000, step=1000)
is_iw = st.sidebar.radio("インスタントウィン", ["有り", "無し"])
update = st.sidebar.number_input("ページ更新回数", min_value=0, value=1)

# 算出ボタン
st.sidebar.markdown("---")
submit = st.sidebar.button("🚀 見積もりを算出")

# 3. 計算と表示
if submit:
    j_months = period + 1
    m_count = winners * 2
    m_cost = m_count * 1000
    iw_cost = 3000000 if is_iw == "有り" else 0
    init = 4550000 + iw_cost + m_cost
    oper = (650000 * period) + (400000 * j_months) + (1000000 * update)
    
    st.header(f"合計費用（税抜）: {init + oper:,}円")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### **■ 初期費用**")
        st.write(f"・初期設定/レシート実装: 4,500,000円")
        st.write(f"・IW実装費: {iw_cost:,}円")
        st.write(f"・目検作業費 ({m_count:,}枚): {m_cost:,}円")
        st.write("・抽選費用: 50,000円")
    with c2:
        st.markdown("### **■ 運用費用**")
        st.write(f"・システム月額: {650000*period:,}円")
        st.write(f"・事務局対応: {400000*j_months:,}円")
        st.write(f"・ページ更新: {1000000*update:,}円")

    st.divider()
    st.info("💡 算出根拠: 事務局費は期間+1ヶ月、目検費は当選数の2倍で計算しています。")
    st.warning("⚠️ **注釈：LP制作費、告知LINE配信費、賞品代は含まれません。**")
else:
    st.info("👈 左のボタンを押して見積もりを開始してください。")
