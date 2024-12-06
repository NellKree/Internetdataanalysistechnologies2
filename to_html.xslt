<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <style>
                    table {
                        width: 100%;
                        border-collapse: collapse;
                    }
                    th, td {
                        border: 1px solid #dddddd;
                        padding: 8px;
                        text-align: left;
                    }
                    th {
                        background-color: #f2f2f2;
                    }
                    .track-table {
                        width: 100%;
                        border: none;
                    }
                    .track-table th, .track-table td {
                        border: none;
                        padding: 5px;
                    }
                    .track-table th {
                        text-align: center;
                        background-color: #e6e6e6;
                    }
                </style>
            </head>
            <body>
                <h1>Albums Information</h1>
                <table>
                    <tr>
                        <th>Album Title</th>
                        <th>Genres</th>
                        <th>Artists</th>
                        <th>Album Length</th>
                        <th>Release Date</th>
                        <th>Age Restriction</th>
                        <th colspan="3">
                            <table class="track-table">
                                <tr>
                                    <th colspan="3">Tracks</th>
                                </tr>
                                <tr>
                                    <th>#</th>
                                    <th>Name</th>
                                    <th>Duration</th>
                                </tr>
                            </table>
                        </th>
                    </tr>
                    <xsl:for-each select="albums/album">
                        <tr>
                            <td><xsl:value-of select="title"/></td>
                            <td>
                                <xsl:for-each select="genres/genre">
                                    <xsl:value-of select="."/>
                                    <xsl:if test="position() != last()">, </xsl:if>
                                </xsl:for-each>
                            </td>
                            <td>
                                <xsl:for-each select="artists/artist">
                                    <xsl:value-of select="."/>
                                    <xsl:if test="position() != last()">, </xsl:if>
                                </xsl:for-each>
                            </td>
                            <td><xsl:value-of select="album_length"/></td>
                            <td><xsl:value-of select="release_date"/></td>
                            <td><xsl:value-of select="age_restriction"/></td>
                            <td colspan="3">
                                <table class="track-table">
                                    <xsl:for-each select="tracks/track">
                                        <tr>
                                            <td><xsl:value-of select="position()"/></td>
                                            <td><xsl:value-of select="name"/></td>
                                            <td><xsl:value-of select="duration"/></td>
                                        </tr>
                                    </xsl:for-each>
                                </table>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>


