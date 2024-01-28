function add(){
    var h3 = document.getElementById("cart")
    var cart= parseInt(h3.innerText)
    cart++
    h3.innerText=cart
    console.log('working')
}