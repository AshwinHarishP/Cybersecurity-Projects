function checkSSLValidity(details) {
    if (details.url.startsWith("https://")) {
      // Use an external library like `ssl-checker` for comprehensive checks:
      const sslChecker = require('ssl-checker'); // Include the library
      sslChecker.check(details.url).then(result => {
        if (!result.valid) {
          console.warn("SSL certificate issues detected:", result.errors);
          // Send message to background script with details
          chrome.runtime.sendMessage({ action: "handleSslIssues", details });
        }
      });
    }
  }
  
  function checkWebsiteReputation(websiteUrl, callback) {
    // **Replace with your actual implementation using an external reputation API:**
    // Choose a suitable API like VirusTotal, Web of Trust, or build your own integration.
    const apiUrl = "https://YOUR_API_ENDPOINT"; // Replace with your API URL
    const apiKey = "YOUR_API_KEY"; // Replace with your API key (if required)
  
    fetch(apiUrl + "?url=" + websiteUrl, {
      headers: { "Authorization": apiKey ? `Bearer ${apiKey}` : undefined } // Set headers if needed
    })
    .then(response => response.json())
    .then(data => {
      // Extract relevant reputation information from the API response (e.g., risk score, details)
      const isTrusted = processReputationData(data); // Implement your logic to determine trust
      callback(isTrusted);
    })
    .catch(error => {
      console.error("Error fetching reputation data:", error);
      // Handle API errors gracefully
    });
  }
  
  chrome.webNavigation.onErrorOccurred.addListener(checkSSLValidity);
  
  // Listen for reputation check requests from popup.js
  chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "checkReputation") {
      const websiteUrl = request.websiteUrl;
      checkWebsiteReputation(websiteUrl, function(isTrusted) {
        sendResponse({ isTrusted });
      });
      return true; // Indicates that sendResponse will be called asynchronously
    }
  });
  