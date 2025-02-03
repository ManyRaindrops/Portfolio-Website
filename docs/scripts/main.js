const navActions = {
  homeButton: './index.html',
  aboutButton: './about.html',
  projectsButton: './projects.html',
  resumeButton: './resume.html',
  notesButton: './notes.html',
  journalButton: './journal.html',
  githubButton: 'https://github.com/ManyRaindrops',
  linkedinButton: 'https://www.linkedin.com/in/bertrand-lee-76624b322/'
};

document.addEventListener('DOMContentLoaded', () => {
  // Mobile menu toggle
  document.querySelector('.gen-nav-menu').addEventListener('click', () => {
    document.querySelector('.header-links').classList.toggle('active');
  });

  // Navigation and social buttons
  Object.entries(navActions).forEach(([id, url]) => {
    const btn = document.getElementById(id);
    if (btn) btn.addEventListener('click', () => {
      url.startsWith('http') ? window.open(url, '_blank') : window.location.href = url;
    });
  });

  // Theme handling
  const themeElements = {
    themesButton: toggleDropdown,
    auto: () => selectTheme('auto'),
    dark: () => selectTheme('dark'),
    light: () => selectTheme('light'),
    grayscale: () => selectTheme('grayscale'),
    shadow: () => selectTheme('shadow')
  };

  Object.entries(themeElements).forEach(([id, handler]) => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('click', handler);
  });

  // Initialize saved theme
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    selectTheme(savedTheme, false);
  } else {
    // Apply system preference if no theme is saved
    applySystemThemePreference();
  }
});

// Theme functions
function toggleDropdown() {
  document.querySelector('.dropdown').classList.toggle('show');
}

function selectTheme(themeName, shouldToggle = true) {
  if (themeName === 'auto') {
    applySystemThemePreference();
  } else {
    document.body.className = `theme-${themeName}`;
    localStorage.setItem('theme', themeName);
  }
  if (shouldToggle) toggleDropdown();
}

function applySystemThemePreference() {
  const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const themeName = prefersDarkScheme ? 'dark' : 'light';
  document.body.className = `theme-${themeName}`;
}

window.addEventListener('click', (e) => {
  const dropdown = document.querySelector('.dropdown');
  if (!e.target.closest('#theme-selector') && dropdown.classList.contains('show')) {
    dropdown.classList.remove('show');
  }
});

const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    selectTheme(savedTheme, false);
}