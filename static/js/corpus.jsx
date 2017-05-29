import React from 'react';
import ReactDOM from 'react-dom';

export class CorpusList extends React.Component {

    render() {
        return (
            <div>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Number</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.data.map(corpus => (
                            <tr key={corpus.id}>
                                <td>{corpus.id}</td>
                                <td>{corpus.number}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    }

}