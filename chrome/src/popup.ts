import * as moment from "moment";
import * as $ from "jquery";

let count = 0;

var tabStatusMap = {};

function handleWindowLoad() {
  console.log("i was loaded");
}

$(function () {
  handleWindowLoad();

  const queryInfo = {
    active: true,
    currentWindow: true,
  };

  chrome.tabs.query(queryInfo, function (tabs) {
    // $('#url').text(tabs[0].url);
    // $('#time').text(moment().format('YYYY-MM-DD HH:mm:ss'));
    if (!Object.keys(tabStatusMap).includes(tabs[0].id.toString())) {
      tabStatusMap[tabs[0].id] = false;
    }
    chrome.tabs.sendMessage(
      tabs[0].id,
      {
        isNeutralised: tabStatusMap[tabs[0].id],
      },
      function (msg) {
        console.log(msg);
      }
    );
    tabStatusMap[tabs[0].id] = true;
  });

  chrome.browserAction.setBadgeText({ text: count.toString() });
  $("#countUp").click(() => {
    chrome.browserAction.setBadgeText({ text: (++count).toString() });
  });

  $("#changeBackground").click(() => {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(
        tabs[0].id,
        {
          color: "#555555",
        },
        function (msg) {
          console.log("result message:", msg);
        }
      );
    });
  });
});
