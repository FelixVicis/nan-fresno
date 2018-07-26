$(document).ready(function () {
  //particles
  particlesJS("particles-js", {"particles":{"number":{"value":150,"density":{"enable":true,"value_area":800}},"color":{"value":"#fff"},"shape":{"type":"circle","stroke":{"width":0,"color":"#000000"},"polygon":{"nb_sides":5},"image":{"src":"img/github.svg","width":100,"height":100}},"opacity":{"value":0.5,"random":false,"anim":{"enable":false,"speed":1,"opacity_min":0.1,"sync":false}},"size":{"value":3,"random":true,"anim":{"enable":false,"speed":40,"size_min":0.1,"sync":false}},"line_linked":{"enable":true,"distance":150,"color":"#fff","opacity":0.4,"width":1},"move":{"enable":true,"speed":6,"direction":"none","random":false,"straight":false,"out_mode":"out","bounce":false,"attract":{"enable":false,"rotateX":600,"rotateY":1200}}},"interactivity":{"detect_on":"canvas","events":{"onhover":{"enable":true,"mode":"repulse"},"onclick":{"enable":true,"mode":"push"},"resize":true},"modes":{"grab":{"distance":400,"line_linked":{"opacity":1}},"bubble":{"distance":400,"size":40,"duration":2,"opacity":8,"speed":3},"repulse":{"distance":200,"duration":0.4},"push":{"particles_nb":4},"remove":{"particles_nb":2}}},"retina_detect":true});

  //scroll magic
  var controller = new ScrollMagic.Controller();


  new ScrollMagic.Scene({
          triggerElement: ".firstsection",
          triggerHook: "onLeave",

      })
      .setPin(".firstsection")
      //.addIndicators() // add indicators (requires plugin)
      .addTo(controller);


      new ScrollMagic.Scene({
        triggerElement: ".secondsection",
        triggerHook: "onLeave",
      })
      .setPin(".secondsection")
      .addTo(controller);


      // third scene
      // var fromTopTimeline = new TimelineMax();
      // var fromTopFrom = TweenMax.from("#top", 1, {
      //   x: -500
      // });
      // var fromTopTo = TweenMax.to("#top", 1, {
      //   x: 0
      // });
      // fromTopTimeline
      // .add(fromTopFrom)
      // .add(fromTopTo);

  // new ScrollMagic.Scene({
  //   triggerElement: ".thirdsection",
  //   offset: 500,
  // })
  // .setPin(".thirdsection")
  // .on(setTimeout(function(){
  //   odometer.innerHTML = 3000;
  // }, 1000))
  // .duration(500)

  // .addTo(controller);

// new ScrollMagic.Scene({
//         triggerElement: "#slidein2",
//         triggerHook: "onLeave",
//     })
//     .setPin("#slidein2")
//     .setTween(fromLeftTimeline)
//     .duration(100)
    //    .reverse(false)
    //.addIndicators() // add indicators (requires plugin)
    // .addTo(controller);

  // setTimeout(function(){
  //   odometer.innerHTML = 3000;
  // }, 1000);

});
