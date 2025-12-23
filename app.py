import streamlit as st
import google.generativeai as genai

# 1. ページ基本設定
st.set_page_config(page_title="AI見積エージェント", layout="wide")
st.title("🎯 キャンペーン戦略・見積AIエージェント")

# 2. APIキー設定
genai.configure(api_key="AIzaSyAFsilIzfMzV2oBZWeanWEIkTYlH7ePwZ0")

# 3. 入力エリア
st.markdown("### 📋 キャンペーン情報を貼り付けてください")
minutes = st.text_area("「施策期間」「当選者数」などの情報をここに貼ってください", height=200)

if st.button("🚀 見積・分析を開始する"):
    if not minutes.strip():
        st.warning("⚠️ 内容が空欄です！情報を入力してください。")
    else:
        # モデル名を最新版に固定
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner("貴社専用ロジックで計算中..."):
            tab1, tab2, tab3 = st.tabs(["📊 詳細見積書", "👥 ターゲット分析", "📝 ヒアリング事項"])
            
            logic = """
            あなたは熟練のプランナーです。以下の単価ルールを厳守して見積を作成してください。
            【1. 絶対にかかる初期費用】
            ・Fanspot 初期設定費用: 3,500,000円
            ・Fanspot レシート応募実装費: 1,000,000円
            ・Fanspot レシートOCR即時解析: 3,000,000円
            ・FanSpot インスタントウィン機能実装費: 3,000,000円（※有りの場合のみ）
            ・目検作業費: 1枚1,000円。当選者数の2倍の枚数で算出。
            ・抽選費用: 50,000円/回
            【2. CP期間に連動する費用】
            ・Fanspot 月額費用: 650,000円 × 施策期間(月数)
            ・問合せ事務局対応費: 400,000円 × (施策期間 + 1ヶ月)
            ・FanSpot ページ更新費: 1,000,000円 × 更新回数
            """
            
            try:
                with tab1:
                    res1 = model.generate_content(f"{logic}\n\n条件：\n{minutes}")
                    st.markdown(res1.text)
                    st.divider()
                    st.warning("⚠️ **注釈：上記見積には、LINE配信費用および制作費用は含まれておりません。**")
                with tab2:
                    res2 = model.generate_content(f"ペルソナを3名作成して：\n{minutes}")
                    st.markdown(res2.text)
                with tab3:
                    res3 = model.generate_content(f"ヒアリング項目を5つ提案して：\n{minutes}")
                    st.markdown(res3.text)
            except Exception as e:
                st.error(f"実行中にエラーが発生しました: {e}")
