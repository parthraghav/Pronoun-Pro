import React, { useRef, useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

const Container = ({
  type,
  text,
  scrollYPosition,
  setScrollYPosition,
}: {
  type: string;
  text: string;
  scrollYPosition: number;
  setScrollYPosition: any;
}) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const handleScroll = () => {
    const containerEl = containerRef.current;
    if (containerEl) {
      setScrollYPosition(containerEl.scrollTop);
    }
  };
  const setScroll = () => {
    const containerEl = containerRef.current;
    if (containerEl) {
      containerEl.scrollTop = scrollYPosition;
    }
  };
  setScroll();
  return (
    <div
      className={type == "input" ? "inputContainer" : "outputContainer"}
      ref={containerRef}
      onScroll={() => handleScroll()}
    >
      {text}
    </div>
  );
};

function App() {
  const [scrollYPosition, setScrollYPosition] = useState(0);
  const [text, setText] = useState(`
  Contrary to popular belief, Lorem Ipsum is not simply random text. It has
  roots in a piece of classical Latin literature from 45 BC, making it over
  2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney
  College in Virginia, looked up one of the more obscure Latin words,
  consectetur, from a Lorem Ipsum passage, and going through the cites of
  the word in classical literature, discovered the undoubtable source. Lorem
  Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et
  Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This
  book is a treatise on the theory of ethics, very popular during the
  Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit
  amet..", comes from a line in section 1.10.32. The standard chunk of Lorem
  Ipsum used since the 1500s is reproduced below for those interested.
  Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by
  Cicero are also reproduced in their exact original form, accompanied by
  English versions from the 1914 translation by H. Rackham. There are many
  variations of passages of Lorem Ipsum available, but the majority have
  suffered alteration in some form, by injected humour, or randomised words
  which don't look even slightly believable. If you are going to use a
  passage of Lorem Ipsum, you need to be sure there isn't anything
  embarrassing hidden in the middle of text. All the Lorem Ipsum generators
  on the Internet tend to repeat predefined chunks as necessary, making this
  the first true generator on the Internet. It uses a dictionary of over 200
  Latin words, combined with a handful of model sentence structures, to
  generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is
  therefore always free from repetition, injected humour, or
  non-characteristic words etc.
  `);
  return (
    <div className="app">
      <div className="controllerContainer">
        <div className="row">
          <input
            className="searchBar"
            type="text"
            placeholder="Enter URL for the website you want to neutralise"
          />
          <a className="submitBtn">Crawl and Neutralise</a>
        </div>
        <div className="block suggestionsBar">
          <span>Suggestions: </span>
          <div className="suggestionsContainer">
            <a>The Guardian</a>
            <a>IMDb</a>
            <a>National Geographic</a>
            <a>Google News</a>
            <a>Facebook</a>
          </div>
        </div>
      </div>
      <div className="row">
        <div className="wrapper">
          <h3>Original Text</h3>
          <Container
            type="input"
            text={text}
            scrollYPosition={scrollYPosition}
            setScrollYPosition={setScrollYPosition}
          />
        </div>
        <div className="wrapper">
          <h3>Neutralised Text</h3>
          <Container
            type="output"
            text={text}
            scrollYPosition={scrollYPosition}
            setScrollYPosition={setScrollYPosition}
          />
        </div>
      </div>
    </div>
  );
}

export default App;
