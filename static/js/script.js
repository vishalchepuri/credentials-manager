console.log("hello")

let list = [...document.getElementsByClassName('table-row')]
list.forEach((element) => {
    element.addEventListener("click", (e) => {
        window.location.href = "/edit/" + e.target.closest('.table-row').children[0].innerText;
    })
})
