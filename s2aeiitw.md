# Google Form Monitor

This project embeds a Google Form in a webpage and uses JavaScript to detect if a user switches tabs or minimizes the window.

## 🚀 Features

- Embeds a Google Form using an iframe
- Detects when the user:
  - Switches tabs
  - Minimizes the window
- Displays a warning when the tab loses focus
- Simple HTML and JavaScript, easy to customize

## 📦 Files

- `index.html`: Main HTML page with embedded Google Form and tab switching detection logic.

## 🛠️ Setup

1. Replace `YOUR_FORM_ID` in the `iframe` `src` with your actual Google Form ID.
2. Open `index.html` in a browser or host it using GitHub Pages:

### Hosting via GitHub Pages

1. Push this project to a new GitHub repository.
2. Go to **Settings > Pages** in your repository.
3. Under "Source", select the `main` branch and `/ (root)` folder.
4. Visit `https://your-username.github.io/your-repo-name` to view it.

## 🧪 Sample Warning Behavior

When the user switches tabs or minimizes the window, a red warning bar appears at the top of the form.

---

🛡️ **Note**: JavaScript in browsers cannot prevent tab switching due to privacy and security policies. This implementation only detects and reacts to it.

