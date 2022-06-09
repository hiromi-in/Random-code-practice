'use strict';

//Look for prime numbers
let n=parseInt(window.prompt('Please type a number'));

for (let i=2; i<=n; i++){
    for(let j=2; j<=i; j++){
        if(i%j===0) continue
    }
    document.getElementById('prime_number').innerHTML=`<li>${i}</li>`;
}

