import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: 'Loading',
    };
  }

  render() {
    return (
      <ul className="wrapper">
        <h1 className="test">Hello World</h1>
      </ul>
    );
  }
}

export default App;
