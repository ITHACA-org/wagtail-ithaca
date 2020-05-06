window.cookieconsent.initialise({
 container: document.getElementById("content"),
 palette: {
  popup: {
    background: "#606c7b",
    text: "#fff",
  },
  button: {background: "#0063e0"},
 },
 onStatusChange: function(status) {
  console.log(this.hasConsented() ?
   'enable cookies' : 'disable cookies');
 },
 law: {
     regionalLaw: false,
    },
 type: "opt-out",
 content: {
   href: '/about/privacy/',
   allow: '<i class="fas fa-cookie-bite fa-lg"></i> Allow cookies',
 }
});
