// Получаем ссылки на элементы
var myButton = document.getElementById('myButton');
var myPopup = document.getElementById('myPopup');
var closePopup = document.getElementById('closePopup');

if (myButton) {
    myButton.addEventListener("click", function () {
        if (myPopup) {
            myPopup.classList.add("show");
        }
    });
}

if (closePopup) {
    closePopup.addEventListener("click", function () {
        if (myPopup) {
            myPopup.classList.remove("show");
        }
    });
}

window.addEventListener("click", function (event) {
    if (myPopup && event.target == myPopup) {
        myPopup.classList.remove("show");
    }
});

function delete_quesion() {
    if (confirm("Вы уверены?")) {
        document.getElementById('delete_form').submit()
    }
}
