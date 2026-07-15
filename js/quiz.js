function checkAnswer(button, correctIndex){

    const card = button.parentElement;

    const radios = card.querySelectorAll("input");

    let selected = -1;

    radios.forEach((r,index)=>{

        if(r.checked){

            selected=index;

        }

    });

    const result = card.querySelector(".result");

    if(selected==-1){

        result.innerHTML="Select an option.";

        result.style.color="orange";

        return;

    }

    if(selected==correctIndex){

        result.innerHTML="✅ Correct!";

        result.style.color="green";

    }

    else{

        result.innerHTML="❌ Wrong! Correct Answer: Option "+String.fromCharCode(65+correctIndex);

        result.style.color="red";

    }

}