import React from "react";
import "./App.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faRocket,
  faBook,
  IconDefinition,
} from "@fortawesome/free-solid-svg-icons";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
import { DiscussionEmbed } from "disqus-react";

const ResponsiveBtn = ({
  label,
  icon,
  focused,
}: {
  label: string;
  icon: IconDefinition;
  focused?: boolean;
}) => {
  return (
    <div className={"resp-btn " + (focused ? "resp-btn-focused" : "")}>
      <FontAwesomeIcon icon={icon} />
      <span>{label}</span>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <header className="resp-pos">
        <h1>
          Pronoun <label>PRO</label>
        </h1>
        <h2>Neutralising Gendered Pronouns using Coreference Resolution</h2>
        <h3>Parth Raghav</h3>
        <hr />
      </header>
      <p className="resp-pos">
        Lorem Ipsum is simply dummy text of the printing and typesetting
        industry. Lorem Ipsum has been the industry's standard dummy text ever
        since the 1500s, when an unknown printer took a galley of type and
        scrambled it to make a type specimen book. It has survived not only five
        centuries, but also the leap into electronic typesetting, remaining
        essentially unchanged. It was popularised in the 1960s with the release
        of Letraset sheets containing Lorem Ipsum passages, and more recently
        with desktop publishing software like Aldus PageMaker including versions
        of Lorem Ipsum.
      </p>
      <p className="resp-pos">
        Contrary to popular belief, Lorem Ipsum is not simply random text. It
        has roots in a piece of classical Latin literature from 45 BC, making it
        over 2000 years old. Richard McClintock, a Latin professor at
        Hampden-Sydney College in Virginia, looked up one of the more obscure
        Latin words, consectetur, from a Lorem Ipsum passage, and going through
        the cites of the word in classical literature, discovered the
        undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33
        of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by
        Cicero, written in 45 BC. This book is a treatise on the theory of
        ethics, very popular during the Renaissance. The first line of Lorem
        Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section
        1.10.32.
      </p>
      <iframe
        className="resp-iframe"
        src="https://www.youtube.com/embed/ZKkLR-Jmjwo"
        frameBorder="0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      ></iframe>
      <div className="resp-pos">
        <div className="resp-btn-container">
          <ResponsiveBtn label="Live Server" icon={faRocket} focused={true} />
          <ResponsiveBtn label="Source Code" icon={faGithub} />
          <ResponsiveBtn label="Extended Abstract" icon={faBook} />
        </div>
      </div>
      <div className="resp-pos">
        <DiscussionEmbed
          shortname="parthraghav"
          config={{
            url: "http://localhost:3000/",
            identifier: "pronoun_pro",
            title: "Pronoun Pro",
            language: "en_US",
          }}
        />
      </div>
    </div>
  );
}

export default App;
