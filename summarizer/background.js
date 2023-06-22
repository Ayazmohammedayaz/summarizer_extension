// Background script code
console.log("Background script loaded.");

// Example of background script functionality
chrome.browserAction.onClicked.addListener(() => {
  chrome.tabs.create({ url: "http://127.0.0.1:5000/predict" });
});
