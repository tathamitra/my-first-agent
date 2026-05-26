// Ahoy! Welcome aboard the Login API ship, matey! ⚓
const express = require('express');

const app = express();

// Arrr! We be parsin' JSON from the request body, ye scallywag!
app.use(express.json());

// Avast! Here be the placeholder login endpoint, sail ho!
app.post('/api/login', (req, res) => {
  const { username, password } = req.body;

  // Shiver me timbers! Check if the crew sent proper credentials
  if (!username || !password) {
    return res.status(400).json({
      success: false,
      message: 'Username and password be required, ye landlubber!'
    });
  }

  // Ye be warned, matey! This be a placeholder — no real auth here!
  return res.status(200).json({
    success: true,
    message: 'Login successful',
    token: 'placeholder-token'
  });
});

// Here be dragons! The server sets sail on port 3000
const PORT = process.env.PORT || 3000;

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server be sailin' on port ${PORT}! Yo ho ho!`);
  });
}

// Export fer testin' purposes, arrr!
module.exports = app;
