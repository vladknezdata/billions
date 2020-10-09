import React from 'react'
import Reference from './Reference'
import Seasons from './Seasons'
import Blog from './Blog'

class MainContainer extends React.Component {

    render (props) {
        const references = this.props.state.referenceList.map(ref => <Reference key= {ref.id} reference={ref} />)
        if (this.props.typeOfWindow === 'references')
        return (
            <div>
                {references}
            </div>
        );
        else if (this.props.typeOfWindow === 'seasons')
        return (
            <div>
                <Seasons />
            </div>
        );
         else if (this.props.typeOfWindow === 'blog')
        return (
            <div>
                <Blog />
            </div>
        )
    }
}

export default MainContainer;