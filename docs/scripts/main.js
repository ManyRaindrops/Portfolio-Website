const switcher = document.querySelector('#theme-switcher')
const doc = document.firstElementChild

const setTheme = theme => {
  console.log(`Setting theme to: ${theme}`)
  if (theme === 'auto') {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    theme = prefersDark ? 'dark' : 'light'
  }
  doc.setAttribute('color-scheme', theme)
}

switcher.addEventListener('input', e => {
  console.log(`Theme switcher input: ${e.target.value}`)
  setTheme(e.target.value)
})

const topButton = document.querySelector('#Top')
const bottomButton = document.querySelector('#Bottom')

if (topButton) {
  topButton.addEventListener('click', () => {
    console.log('Move Up button clicked')
    window.scrollTo(0, 0)
  })
} else {
  console.error('Top button not found')
}

if (bottomButton) {
  bottomButton.addEventListener('click', () => {
    console.log('Move Down button clicked')
    window.scrollTo(0, document.body.scrollHeight)
  })
} else {
  console.error('Bottom button not found')
}

// Ensure the theme is set based on the initial selection
const initialTheme = switcher.querySelector('input:checked').value
console.log(`Initial theme: ${initialTheme}`)
setTheme(initialTheme)
