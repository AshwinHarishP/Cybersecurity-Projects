document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('checkButton').addEventListener('click', checkSafety);
  });
  
  function checkSafety() {
    var websiteUrl = document.getElementById('websiteInput').value;

    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        const activeTab = tabs[0];
        chrome.runtime.sendMessage({ action: "checkReputation", websiteUrl }, function(response) {
            if (response && !response.isTrusted) {
                document.getElementById('result').textContent = "Website is potentially unsafe!";
            } else {
                document.getElementById('result').textContent = "Website seems safe based on current checks.";
            }
        });
    }); 
}