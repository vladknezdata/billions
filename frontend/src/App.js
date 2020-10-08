import React from 'react';
import './App.css';

class App extends React.Component {
    constructor () {
        super()
        this.state = {
            referenceList: []
        }
        this.fetchReferences = this.fetchReferences.bind(this)
    }
    
    componentDidMount() {
        this.fetchReferences()
    }

    fetchReferences() {
        console.log('Fethcing...')
        fetch('http://127.0.0.1:8000/api/reference-list/')
        .then(response => response.json())
        .then(data =>
            this.setState({
                referenceList: data
            })
        )
    }


    render () {
        console.log(this.state.referenceList.length > 0 ? this.state.referenceList : 'Loading...')

        return (
            <div></div>
        )
    }
}


export default App;
