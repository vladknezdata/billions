import React from 'react'

class Loading extends React.Component {

    render() {
        return (
            <div>
                <div className="spinner-grow" role="status">
                    <span className="sr-only">Loading...</span>
                </div>
            </div>
        )
    }
}

export default Loading;