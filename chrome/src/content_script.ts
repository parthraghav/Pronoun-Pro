import * as $ from "jquery";

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
  console.log(input);
  $.ajax(settings).done(function (response) {
    var result = response.result;
    console.log(result);
    if (parseInt(response.status) == 200) {
      manipulateDOMWithResult(result);
    }
  });
}

window.onload = handleWindowLoad;
