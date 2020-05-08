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
 content: {
   message: "We use our own and third-party cookies to improve your experience and our services. By continuing and using the site, including by remaining on the landing page, you consent to the use of cookies. Click here for more information on our Cookie Policy",
   href: '/about/privacy/',
  dismiss: '<i class="fas fa-cookie-bite fa-lg"></i> Allow cookies',
 }
});
