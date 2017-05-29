import React from 'react';
import ReactDOM from 'react-dom';

export class GroupList extends React.Component {

    render() {
        return (
            <div>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Code</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.data.map(group => (
                            <tr key={group.id}>
                                <td>{group.id}</td>
                                <td>{group.code}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    }

}