const assert=require('node:assert/strict');
const C=require('./dist/prace/shared/core.js');
assert.deepEqual(C.totals([{price:249,qty:2},{price:129,qty:1}],.1,15),{subtotal:627,reduction:62.7,total:579.3});
assert.deepEqual(C.totals([],0,0),{subtotal:0,reduction:0,total:0});
assert.equal(C.totals([{price:19.99,qty:3}],.1,12).total,65.97);
assert.deepEqual(C.budget([{amount:640},{amount:240},{amount:280}],1800),{spent:1160,left:640,percent:1160/1800*100});
assert.deepEqual(C.budget([{amount:200}],100),{spent:200,left:-100,percent:100});
assert.equal(C.escape('<img src=x onerror="bad">'), '&lt;img src=x onerror=&quot;bad&quot;&gt;');
console.log('PASS: cart totals, discount rounding, empty cart, budget, overspending, HTML escaping');
