function scuberGreetingForFeet(){
  // Write your code here!
  (scuberGreetingForFeet(199)).to.equal('This one is on me!');

}

function ternaryCheckCity(){
  // Write your code here!
  (ternaryCheckCity('NYC')).to.equal('Ok, sounds good.');
}


function switchOnCharmFromTip(){
  it('should return "Thank you so much." if the tip is generous', function () {
    expect(switchOnCharmFromTip('generous')).to.equal('Thank you so much.');
}
