document.addEventListener('DOMContentLoaded',()=>{
 const burger=document.querySelector('.hamburger'),nav=document.querySelector('.nav-links');
 burger.addEventListener('click',()=>nav.classList.toggle('active'));
});