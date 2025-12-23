import streamlit as st

# 1. ページ基本設定
st.set_page_config(page_title="Fanspot見積システム", layout="wide")
st.title("🎯 Fanspot 案件見積エージェント")

# 2. サイドバーに入力項目（OCRを削除）
st.sidebar.header("📋 条件入力")
period = st.sidebar.number_input("施策期間 (月数)", min_value=1, value=2)
winners = st.sidebar.number_input("当選者数", min_value=0, value=10000, step=1000)
is_iw = st.sidebar.radio("インスタントウィン", ["有り", "無し"])
update = st.sidebar.number_input("ページ更新回数", min_value=0, value=1)

# 3. 見積算出ロジック
if st.sidebar.button("🚀 見積もりを算出"):
    # 事務局と目検のロジック計算
    j_months = period + 1
    m_count = winners * 2
    m_cost = m_count * 1000
    
    # OCR解析費は一律0円または削除の扱い
    ocr_cost = 0 
    iw_cost = 3000000 if is_iw == "有り" else 0
    
    # 各種費用の合計
    init = 3500000 + 1000000 + ocr_cost + iw_cost + m_cost + 50000
    oper = (650000 * period) + (400000 * j_months) + (1000000 * update)
    total = init + oper

    # 4. 画面表示
    st.header(f"合計費用（税抜）: {total:,}円")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**■ 初期費用: {init:,}円**")
        st.write(f"・設定/実装: 4,500,000円\n・IW実装: {iw_cost:,}円\n・目検作業 ({m_count:,}枚): {m_cost:,}円\n・抽選費用: 50,000円")
    with col2:
        st.markdown(f"**■ 運用費用: {oper:,}円**")
        st.write(f"・月額費用: {650000*period:,}円\n・事務局対応 ({j_months}ヶ月): {400000*j_months:,}円\n・ページ更新 ({update}回): {1000000*update:,}円")
    
    st.divider()
    # 5. 注釈の追記
    st.warning("⚠️ **注釈：上記見積には、LINE配信費用、クリエイティブ制作費用、および「賞品代」「発送費」は含まれておりません。**")
else:
    st.info("左側のメニューで条件を選び、ボタンを押してください。")
