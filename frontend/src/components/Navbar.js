import React from 'react'
import MainContainer from './MainContainer'


class Navbar extends React.Component {
    constructor(props) {
        super(props)
        this.state = this.props.state
        this.handleClick = this.handleClick.bind(this)
    }

    handleClick(e) {
        console.log('Clickety click')
        const typeOfWindow = e.target.getAttribute('typeOfWindow')
        console.log('TOW: ', typeOfWindow)
        this.setState({
                typeOfWindow: typeOfWindow
        })
    }
    render(props) {

        return (
            <div className="nav-scroller py-1 mb-2">
            <nav className="nav d-flex justify-content-between">
                <a onClick={(e) => this.props.handleMainWindow('blog')} className="p-2 text-muted">Blog</a>
                <a onClick={this.props.getReferences} name='season' value={this.props.state.season} className="p-2 text-muted">References</a>
                <a onClick={(e) => this.props.handleMainWindow('seasons')} className="p-2 text-muted" >Seasons</a>
                <a className="p-2 text-muted" href="{% url 'references:characters' %}">Characters</a>
                <a className="p-2 text-muted" href="#">Songlist</a>
            </nav>
        </div>
        )
    }
}
export default Navbar;