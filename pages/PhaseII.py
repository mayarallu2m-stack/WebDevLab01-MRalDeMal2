import streamlit as st

st.title("Which Pasta Type Do You Most Resemble?")
st.write("Answer the my questions to discover your pasta self!")


question_one = st.multiselect("1. How would your friends describe you? ", ["Adventurous", "Loyal", "Creative", "Reliable", "Spontaneous", "Caring"]) #NEW

question_two = st.radio("2. What's your favorite sauce?", ["Marinara", "Alfredo", "Pesto", "No sauce"]) #NEW

question_three = st.number_input("3. How much do you like being the center of attention on a scale of 1-10? ", 1, 10, 1) #NEW

question_four = st.slider("4. How boujie are you on a scale of 1-10? ", 1, 10, 1) #NEW

question_five = st.radio("5. Which city is your dream vacation? ", ["Rome", "Paris", "Barcelona", "London"])


def pasta_type():
    ravioli = 0
    macaroni = 0
    spaghetti = 0
    penne = 0

    
    ## Ravioli Section
    if "Adventurous" in question_one:
        ravioli += 1
    if "Spontaneous" in question_one:
        ravioli += 1
    if question_two == "No sauce":
        ravioli += 1
    if question_three >= 6 and question_three <= 8:
        ravioli += 1
    if question_four >= 6 and question_four <= 8:
        ravioli += 1
    if question_five == "Barcelona":
        ravioli += 1
    
    ## Macaroni Section
    if "Creative" in question_one:
        macaroni += 1
    if "Caring" in question_one:
        macaroni += 1
    if question_two == "Alfredo":
        macaroni += 1
    if question_three >= 1 and question_three <= 2:
        macaroni += 1
    if question_four >= 1 and question_four <= 2:
        macaroni += 1
    if question_five == "London":
        macaroni += 1

    ## Spaghetti Section
    if "Loyal" in question_one:
        spaghetti += 1
    if question_two == "Marinara":
        spaghetti += 1
    if question_three >= 9 and question_three <= 10:
        spaghetti += 1
    if question_four >= 9 and question_four <= 10:
        spaghetti += 1
    if question_five == "Paris":
        spaghetti += 1

    ## Penne Section
    if "Reliable" in question_one:
        penne += 1
    if question_two == "Pesto":
        penne += 1
    if question_three >= 3 and question_three <= 5:
        penne += 1
    if question_four >= 3 and question_four <= 5:
        penne += 1
    if question_five == "Rome":
        penne += 1
    
    result = ""

    if ravioli >= macaroni and ravioli >= spaghetti and ravioli >= penne:
        result = "Ravioli"
    elif macaroni >= ravioli and macaroni >= spaghetti and macaroni >= penne:
        result = "Macaroni"
    elif spaghetti >= ravioli and spaghetti >= macaroni and spaghetti >= penne:
        result = "Spaghetti"
    else:
        result = "Penne"
    
    return ravioli, macaroni, spaghetti, penne, result

if st.button("Calculate my Pasta Type!"):
    ravioli, macaroni, spaghetti, penne, result = pasta_type()
    
    if result == "Ravioli":
        st.image("Images/ravioli.jpg", width=300)
    elif result == "Macaroni":
        st.image("Images/macaroni.jpg", width=300)
    elif result == "Spaghetti":
        st.image("Images/spaghetti.jpg", width=300)
    elif result == "Penne":
        st.image("Images/penne.jpg", width=300)
    
    st.write(f"Scores: Ravioli: {ravioli}, Macaroni: {macaroni}, Spaghetti: {spaghetti}, Penne: {penne}")
    st.success(f"You are most like: **{result}**!")
    st.balloons()
pasta_type()
