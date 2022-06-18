console.log("hello")

let list = [...document.getElementsByTagName('tr')]
list.forEach((element) => {
    element.addEventListener("click", (e) => {
        window.location.href = "/edit/" + e.target.parentElement.children[0].innerText;
    })
})