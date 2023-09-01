// creation of a varible that holds btn click
let btn = 0;
// geting the element 
document.getElementById('btnn').addEventListener('click', () => {
   // updating the varible
   btn++
   // rewriting the element
   document.getElementById('ww').textContent = "vistor count: " + btn;
    
})
