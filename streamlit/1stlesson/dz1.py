import streamlit as st

st.title("Міні-тест на знання Python")
st.write("Перевір свої знання Python! Дай відповіді на 3 запитання.")
st.subheader("1. Яка команда виводить текст на екран?")
q1 = st.radio(
    "Обери правильну відповідь:",
    ["input()", "print()", "output()"],
    key="q1"
)

st.subheader("2. Який тип даних має значення 10?")
q2 = st.radio(
    "Обери правильну відповідь:",
    ["str", "float", "int"],
    key="q2"
)

st.subheader("3. Який символ використовується для коментарів у Python?")
q3 = st.radio(
    "Обери правильну відповідь:",
    ["//", "#", "/* */"],
    key="q3"
)

if st.button("Перевірити результати"):
    key_answers = {"q1": "print()","q2": "int","q3": "#"}

    user_answers = {"q1": q1,"q2": q2,"q3": q3}

    score = sum(user_answers[key] == key_answers[key]for key in key_answers)

    total = len(key_answers)
    percentage = score / total

    st.divider()
    st.subheader("Результати тесту")

    st.write(f"Правильних відповідей: {score} із {total}")
    st.write(f"Фінальний бал: {score}/{total}")

    if score == total:
        st.success("Вітаємо! Усі відповіді правильні!")
    elif score >= 2:
        st.info("Чудовий результат! Майже все правильно.")
    else:
        st.warning("Спробуй ще раз — ти можеш краще!")
