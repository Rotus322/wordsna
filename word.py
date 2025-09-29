import streamlit as st
import random

st.set_page_config(page_title="ワードスナイパー", layout="centered")

HIRAGANA = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞだでどばびぶべぼぱぴぷぺぽ")
THEMES   = ["果物", "動物", "食べ物", "国名", "乗り物","お菓子","都道府県","学校で使うもの","夏と言えば","春と言えば","冬と言えば","秋と言えば","職業","スポーツ","野菜","キャラクター","小学校の時に流行ったもの","高校時代に流行ったもの","チェーン店","理系用語","医療用語","物語","怖いもの","芸能人","歴史で習った言葉"]

# ---------------------------
# セッション初期化
# ---------------------------
if "char" not in st.session_state:
    st.session_state.char = ""
if "theme" not in st.session_state:
    st.session_state.theme = ""
if "players" not in st.session_state:
    st.session_state.players = []          # 登録済プレイヤー名リスト
if "scores" not in st.session_state:
    st.session_state.scores = {}           # {名前: スコア}

st.title("🎯 ワードスナイパー")

# ---------------------------
# プレイヤー登録
# ---------------------------
st.subheader("プレイヤー登録")
new_name = st.text_input("新しいプレイヤー名")
if st.button("追加"):
    name = new_name.strip()
    if name:
        if name not in st.session_state.players:
            st.session_state.players.append(name)
            st.session_state.scores[name] = 0
        else:
            st.warning("その名前は既に登録されています")

# ---------------------------
# カードめくり
# ---------------------------
def draw_card():
    st.session_state.char = random.choice(HIRAGANA)
    st.session_state.theme = random.choice(THEMES)

if st.button("カードをめくる", use_container_width=True):
    if st.session_state.players:
        draw_card()
    else:
        st.warning("プレイヤーを登録してください")

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
# プレイヤーごとのポイント加算ボタン
# ---------------------------
if st.session_state.players:
    st.subheader("プレイヤー別ポイント加算")
    # 2列ずつ並べる例（人数が多い場合は横スクロール）
    cols = st.columns(2)
    for i, name in enumerate(st.session_state.players):
        col = cols[i % 2]
        with col:
            if st.button(f"＋1点 {name}", key=f"add_{name}"):
                st.session_state.scores[name] += 1

# ---------------------------
# スコアボード
# ---------------------------
if st.session_state.scores:
    st.subheader("📊 スコアボード")
    for name, score in sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True):
        st.write(f"**{name}** ： {score} pt")
