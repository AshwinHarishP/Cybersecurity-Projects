chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "handleSslIssues") {
      // Display specific warnings in popup based on detected SSL issues
      console.log("Handling SSL issues for:", request.details.url);
      // Send message to popup.js with details (use chrome.runtime.sendMessage)
    } else if (request.action === "performAdvancedReputationCheck") {
      // If implemented, handle advanced reputation checks here
      // (e.g., using another API or service)
    }
  });
  