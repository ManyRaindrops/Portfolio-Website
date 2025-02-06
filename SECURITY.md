# Security Policy

## Supported Versions

The latest version of the website is currently supported as of Feburary 6, 2025.

## Reporting a Vulnerability
Follow the example of the following Issue: https://github.com/ManyRaindrops/Portfolio-Website/issues/6#issue-2836704310

Firstly, if there is code, indicate the code in question:
- The current security policy:
- `<meta http-equiv="content-security-policy" content="default-src 'self'; style-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' https: data:; font-src 'self'; connect-src 'self'; manifest-src 'self'; frame-src 'self';>`

(If there is no code, first attempt to describe with text exactly what you did to produce the vulnerability. If possible, include a video recording of your reproduction of the vulnerability event.)

When reporting a vulnerability, be sure to indicate exactly what is wrong:
- `unsafe-inline` allows inline scripts to be run directly in the HTML. Inline scripts bypass CSP protections.
- `unsafe-eval` allows special functions to be run inline, allowing for dynamic compiling and execution of code. This increases attack surfaces.
- Both of these issues increase cross-site scripting attacks and malicious code-injection attacks.

After indicating the issue, describe the solution:
- Solution:
- Remove unsafe-inline and unsafe-eval

Finally, if there is code, indicate the changes that should be made. You can also create a pull request.
The recommended security policy:
<meta http-equiv="content-security-policy" content="default-src 'self'; style-src 'self'; script-src 'self'; img-src 'self' https: data:; font-src 'self'; connect-src 'self'; manifest-src 'self'; frame-src 'self';>
