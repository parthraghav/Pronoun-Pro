import * as $ from "jquery";

// chrome.runtime.onMessage.addListener(function (msg, sender, sendResponse) {
//   console.log(msg);
//   if (msg.color) {
//     console.log("Receive color = " + msg.color);
//     document.body.style.backgroundColor = msg.color;
//     sendResponse("Change color to " + msg.color);
//   } else {
//     sendResponse("Color message is none.");
//   }
//   if (!msg.isNeutralised) {
//     document.body.addEventListener("DOMNodeInserted", function (event) {
//       console.log(event.target);
//       console.log("rabitmouth");
//     });
//   }
// });

function manipulateDOMWithResult(result) {
  Object.keys(result)
    .sort()
    .forEach((key) => {
      let replacement_text = result[key];
      let el: HTMLElement | null = document.querySelector(
        `p[data-paragraph-id="${key}"]`
      );
      if (el instanceof HTMLElement) {
        el.innerText = replacement_text;
      }
    });
}

function handleWindowLoad() {
  let input = {};
  [...document.querySelectorAll("p")].forEach((node, i) => {
    node.setAttribute("data-paragraph-id", i.toString());
    input[i] = node.innerText;
  });
  var settings = {
    url: "http://127.0.0.1:5000/",
    method: "POST",
    timeout: 0,
    headers: {
      "Content-Type": "application/json",
    },
    data: JSON.stringify({ data: input }),
  };

  $.ajax(settings).done(function (response) {
    var result = response.result;
    if (parseInt(response.status) == 200) {
      manipulateDOMWithResult(result);
    }
  });
}

window.onload = handleWindowLoad;
