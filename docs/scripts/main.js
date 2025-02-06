// ===================================================== //
//                                                       //
// BSD 3-Clause License Copyright (c) 2025, Bertrand Lee //
//                                                       //
// ===================================================== //





const searchBar = document.getElementById("search-bar");
const searchInput = document.getElementById("search");
const searchResults = document.getElementById("search-results");
const searchButton = document.getElementById("searchButton");

// Open search bar when button is clicked
searchButton.addEventListener("click", function () {
  searchBar.classList.add("active");
  searchInput.focus();
});

// Close search bar when Escape key is pressed
document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    closeSearch();
  }
});

// Close search bar when clicking outside of it
searchBar.addEventListener("click", function (event) {
  if (event.target === searchBar) {
    closeSearch();
  }
});

// Detect Enter key press in the search input
searchInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    event.preventDefault(); // Prevent form submission (if applicable)
    const query = searchInput.value.trim();

    if (query !== "") {
      searchResults.classList.add("show");
      searchResults.innerHTML = `<p>Results for: "${query}"</p>`; // Example result
    } else {
      searchResults.classList.remove("show");
      searchResults.innerHTML = ""; // Clear results if empty
    }
  }
});

// Function to close search bar
function closeSearch() {
  searchBar.classList.remove("active");
  searchResults.classList.remove("show");
  searchResults.innerHTML = ""; // Clear results when closing
  searchInput.value = ""; // Clear input on close
}










document.addEventListener("DOMContentLoaded", function () {
  const overviewContainer = document.getElementById("page-overview");

  if (!overviewContainer) return; // Exit if container doesn't exist

  overviewContainer.innerHTML = ""; // Clear existing content

  // Select all headings (adjust this if needed)
  const headings = document.querySelectorAll("h2, h3");

  headings.forEach((heading) => {
    if (heading.id === "") {
      heading.id = heading.textContent.toLowerCase().replace(/\s+/g, "-"); // Generate an ID if missing
    }

    // Create a link for each heading
    const link = document.createElement("a");
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent;
    
    link.addEventListener("click", (e) => {
      e.preventDefault(); // Prevent default anchor behavior
      const target = document.getElementById(heading.id);
      if (target) {
        const offset = 100; // Adjust this value based on your layout (e.g., height of fixed header)
        const targetPosition = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({
          top: targetPosition,
          behavior: "smooth", // Smooth scroll
        });
      }
    });

    // Append the link to the overview container
    overviewContainer.appendChild(link);
  });
});










const navActions = {
  homeButton: './index.html',
  aboutButton: './about.html',
  projectsButton: './projects.html',
  resumeButton: './resume.html',
  notesButton: './notes.html',
  journalButton: './journal.html',
  blogButton: './blog.html',
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

  
  Object.entries(navActions).forEach(([id, url]) => {
    const btn = document.getElementById(id);
    if (btn) {
      btn.addEventListener('click', () => {
        if (btn.classList.contains('second-layer')) {
            url.startsWith('http') ? window.open(url, '_blank') : window.location.href = '../' + url;
        } else {
          url.startsWith('http') ? window.open(url, '_blank') : window.location.href = url;
        }
      });
    }
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
  localStorage.setItem('theme', 'auto');
}

window.addEventListener('click', (e) => {
  const dropdown = document.querySelector('.dropdown');
  if (!e.target.closest('#theme-selector') && dropdown.classList.contains('show')) {
    dropdown.classList.remove('show');
  }
});

// Attach event listeners
document.getElementById('themesButton').addEventListener('click', toggleDropdown);

document.querySelectorAll('.dropdown button').forEach(button => {
  button.addEventListener('click', () => {
    selectTheme(button.value);
  });
});

// Restore saved theme on page load
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
  selectTheme(savedTheme, false);
} else {
  applySystemThemePreference();
}