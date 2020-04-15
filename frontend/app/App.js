import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: 'Loading',
    };
  }

  componentDidMount() {
    axios.get('/api/tasks').then(res => {
      this.setState({
        data: res.data
      })
    }).catch(err => console.log(err))
  }

  render() {
    return (
      <ul className="wrapper">
        <h1 className="test">Hello World</h1>
        <h2>HELLOOO</h2>
        <h2>Waaas up</h2>
        <h4>Was up</h4>
        <h5>asssss</h5>
        <h6>Sup</h6>
        <h1>Helloooo</h1>
      </ul>
    );
  }
}

export default App;
