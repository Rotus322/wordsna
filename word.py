import streamlit as st
import random

st.set_page_config(page_title="ワードスナイパー", layout="centered")

HIRAGANA = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
THEMES = ["果物", "動物", "食べ物", "国名", "乗り物"]

# ---------------------------
# セッション初期化
# ---------------------------
if "char" not in st.session_state:
    st.session_state.char = ""
if "theme" not in st.session_state:
    st.session_state.theme = ""
if "players" not in st.session_state:       # 登録済プレイヤー一覧
    st.session_state.players = []
if "scores" not in st.session_state:        # {名前: スコア}
    st.session_state.scores = {}

st.title("🎯 ワードスナイパー")

# ---------------------------
# プレイヤー登録
# ---------------------------
st.subheader("プレイヤー登録")
new_player = st.text_input("新しいプレイヤー名")
if st.button("追加"):
    name = new_player.strip()
    if name:
        if name not in st.session_state.players:
            st.session_state.players.append(name)
            st.session_state.scores[name] = 0
        else:
            st.warning("その名前は既に登録されています")

# ---------------------------
# アクティブプレイヤー選択
# ---------------------------
if st.session_state.players:
    active_player = st.selectbox("現在のプレイヤーを選択", st.session_state.players)
else:
    active_player = None
    st.info("プレイヤーを追加してください")

# ---------------------------
# ゲーム操作
# ---------------------------
def draw_card():
    st.session_state.char = random.choice(HIRAGANA)
    st.session_state.theme = random.choice(THEMES)

col1, col2 = st.columns(2)
with col1:
    if st.button("カードをめくる", use_container_width=True):
        if active_player:
            draw_card()
        else:
            st.warning("プレイヤーを選んでください")

with col2:
    if st.button("ポイント加算", use_container_width=True):
        if active_player:
            # ボタン1クリックごとに +1
            st.session_state.scores[active_player] += 1
        else:
            st.warning("プレイヤーを選んでください")

# ---------------------------
# カード表示
# ---------------------------
if st.session_state.char:
    st.markdown("---")
    st.markdown(
        f"<div style='font-size:80px;text-align:center;'>{st.session_state.char}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div style='font-size:40px;text-align:center;'>お題：{st.session_state.theme}</div>",
        unsafe_allow_html=True
    )
    st.markdown("---")

# ---------------------------
# スコアボード
# ---------------------------
if st.session_state.scores:
    st.subheader("📊 スコア一覧（クリック回数）")
    for name, score in sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True):
        st.write(f"**{name}** ： {score} 回")
