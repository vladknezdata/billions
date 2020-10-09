import React from 'react'

class Reference extends React.Component {

    render(props) {
        const ref = this.props.reference
        return (
            <div className='reference'>
                <br/>
                <p>Season: {ref.season},
                    Episode: {ref.episode}
                    </p>

                <h3>{ref.title}</h3>
                <p className='dialog'>{ref.dialog}</p>
                <p>{ref.explanation}</p>
                <div>

                </div>
            </div>
        )
    }

}

export default Reference;