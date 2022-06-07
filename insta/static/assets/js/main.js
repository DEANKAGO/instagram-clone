const copyBtns =[...document.getElementsByClassName('copy-btn')]

let previous = null

copyBtns.forEach(btn=> btn.addEventListener('click', ()=>{
  const image = btn.getAttribute('data-landImage.url')
  navigator.clipboard.writeText(image)
  btn.textContent = 'copied'

  if (previous) {
    previous.textContent = 'Copy Link'
  }
  previous = btn

}))