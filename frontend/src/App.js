import React from 'react';
import './App.css';
import './bootstrap.min.css'
import MainContainer from './components/MainContainer'
import Header from './components/Header'
import Navbar from './components/Navbar'
import Loading from './components/Loading'

class App extends React.Component {
    constructor () {
        super()
        this.state = {
            referenceList: [],
            season: 1,
            episode: 1,
            character: 1,
            referenceType: 1,
            typeOfWindow: 'references'
        }
        this.fetchReferences = this.fetchReferences.bind(this)
        this.fetchFilteredReferences = this.fetchFilteredReferences.bind(this)
        this.handleMainWindow = this.handleMainWindow.bind(this)
    }
    
    componentDidMount() {
        this.fetchReferences()
    }

    handleMainWindow(type) {
        this.setState({
            typeOfWindow: type
        })
    }

    fetchReferences() {
        fetch('http://127.0.0.1:8000/api/reference-list/')
        .then(response => response.json())
        .then(data => 
            this.setState({
                referenceList: data,
        }))
    }
    
    fetchFilteredReferences(e) {
        this.handleMainWindow('references')
        const name = e.target.getAttribute('name')
        const value = e.target.getAttribute('value')

        const url = 'http://127.0.0.1:8000/api/reference-list/'
        fetch(url, {
            method: 'GET',
            'Content-type': 'application/json',
        })
        .then(response => response.json())
        .then(data => 
            data.filter(ref => {
                if (ref[name] == value)
                    return ref;
            }))
        .then(data => {
            this.setState({
                referenceList: data,
                [name]: value
            })})

        console.log('Upadted season: ',this.state.season)
            
    }

    render() {
        console.log(this.state.referenceList)
        return (
            <div className='container App'>
                <p onClick={this.fetchFilteredReferences} name='season' value={this.state.season}>API references</p>

                <div className='header'>
                    <Header />
                </div>

                <div className='navbar'>
                    <Navbar 
                        getReferences={this.fetchFilteredReferences}
                        state={this.state}
                        handleMainWindow={this.handleMainWindow} 
                    />
                </div>

                <div className='main-container'>
                    <MainContainer state={this.state} typeOfWindow={this.state.typeOfWindow} />
                </div>


            </div>
        )
    }
}


export default App;
