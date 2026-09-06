import random
import streamlit as st

st.title("🎯 Game Tebak Angka")

if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0

guess = st.number_input(
    "Masukkan tebakanmu (1-100):", min_value=1, max_value=100, step=1
)

if st.button("Tebak!"):
    st.session_state.attempts += 1
    if guess < st.session_state.target:
        st.warning("Terlalu Rendah!")
    elif guess > st.session_state.target:
        st.warning("Terlalu Tinggi!")
    else:
        st.success(
            f"Selamat! Kamu berhasil dalam {st.session_state.attempts} percobaan!"
        )

if st.button("Main Lagi"):
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.rerun()
