/* Commend Counseling — shared behaviour */
(function(){
  'use strict';

  /* ---- mobile nav ---- */
  var tog=document.querySelector('.navtoggle'), links=document.querySelector('.nav-links');
  function closeNav(){
    if(!links) return;
    links.classList.remove('open');
    if(tog) tog.setAttribute('aria-expanded','false');
  }
  if(tog&&links){
    tog.addEventListener('click',function(){
      var open=links.classList.toggle('open');
      tog.setAttribute('aria-expanded',open?'true':'false');
    });
    links.addEventListener('click',function(e){ if(e.target.tagName==='A') closeNav(); });
    document.addEventListener('keydown',function(e){ if(e.key==='Escape') closeNav(); });
    window.addEventListener('resize',function(){ if(window.innerWidth>980) closeNav(); });
  }

  /* ---- parallax layers ---- */
  var layers=[].slice.call(document.querySelectorAll('[data-sp]'));
  layers.forEach(function(el){el.dataset.base=el.style.transform||'';});
  var vh=window.innerHeight, ticking=false;

  function frame(){
    for(var i=0;i<layers.length;i++){
      var el=layers[i], r=el.getBoundingClientRect();
      if(r.bottom>-500&&r.top<vh+500){
        var sp=parseFloat(el.dataset.sp);
        var off=((vh-r.top)-vh*0.5)*sp*0.095;
        el.style.transform=el.dataset.base+' translate3d(0,'+off.toFixed(2)+'px,0)';
      }
    }
    var bg=document.querySelector('.stmt-bg img');
    if(bg){
      var pr=bg.parentNode.getBoundingClientRect();
      if(pr.bottom>0&&pr.top<vh){
        var p=(vh-pr.top)/(vh+pr.height);
        bg.style.transform='translate3d(0,'+((p-0.5)*-70).toFixed(1)+'px,0)';
      }
    }
    ticking=false;
  }
  window.addEventListener('scroll',function(){
    if(!ticking){ticking=true;requestAnimationFrame(frame);}
  },{passive:true});

  /* ---- reveal on scroll ---- */
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  },{threshold:.08,rootMargin:'0px 0px -50px 0px'});
  document.querySelectorAll('.rv').forEach(function(el){io.observe(el);});

  /* ---- headline fit ----
     Only h1/h2. Script labels carry a negative optical margin that permanently
     inflates scrollWidth, which would drive this loop straight to its floor.
     Floored at 70% of the designed size so an overflow bug can never collapse
     a headline to nothing. */
  function fitAll(){
    document.querySelectorAll('h1,h2').forEach(function(el){
      el.style.fontSize='';
      var box=el.parentNode, cs=getComputedStyle(box);
      var avail=box.clientWidth-(parseFloat(cs.paddingLeft)||0)-(parseFloat(cs.paddingRight)||0);
      if(!avail) return;
      var start=parseFloat(getComputedStyle(el).fontSize), size=start, guard=0;
      while(el.scrollWidth>avail+1 && size>start*0.70 && guard++<40){
        size*=0.97; el.style.fontSize=size.toFixed(2)+'px';
      }
    });
  }

  /* ---- hero fits the first screen ---- */
  function fitHero(){
    var hero=document.querySelector('.hero'),
        copy=document.querySelector('.hero-copy'),
        nv=document.querySelector('nav');
    if(!hero||!copy||!nv) return;
    document.documentElement.style.setProperty('--navh', nv.offsetHeight+'px');
    copy.style.setProperty('--hs',1);
    var hs=getComputedStyle(hero);
    var pad=parseFloat(hs.paddingTop)+parseFloat(hs.paddingBottom);
    var avail=window.innerHeight-nv.offsetHeight-pad;
    var scale=1, guard=0;
    while(copy.scrollHeight>avail && scale>0.60 && guard++<30){
      scale-=0.035; copy.style.setProperty('--hs',scale.toFixed(3));
    }
  }

  /* ---- placeholder toggle (dev aid — harmless once .fill spans are gone) ---- */
  var fn=document.querySelector('.fillnote');
  if(fn){
    var n=document.querySelectorAll('.fill').length;
    if(!n){ fn.remove(); }
    else{
      var c=fn.querySelector('[data-count]'); if(c) c.textContent=n;
      var b=fn.querySelector('button');
      if(b) b.addEventListener('click',function(){
        var hid=document.body.classList.toggle('hide-fills');
        b.textContent=hid?'Show placeholders':'Hide placeholders';
      });
    }
  }

  function boot(){ fitAll(); fitHero(); document.body.classList.add('ready'); frame(); }
  if(document.fonts && document.fonts.ready){
    document.fonts.ready.then(boot);
    setTimeout(function(){ if(!document.body.classList.contains('ready')) boot(); },1200);
  } else { boot(); }

  var rt;
  window.addEventListener('resize',function(){
    vh=window.innerHeight;
    clearTimeout(rt); rt=setTimeout(function(){fitAll();fitHero();},140);
  });
})();
