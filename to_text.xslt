<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="text" encoding="UTF-8"/>

    <xsl:template match="/">
        <xsl:value-of select="'Albums List'"/>
        <xsl:text>&#10;</xsl:text>
        <xsl:text>&#10;</xsl:text>

        <xsl:for-each select="albums/album">
            <xsl:value-of select="concat('Album ', number, ': ', title)"/>
            <xsl:text>&#10;</xsl:text>

            <xsl:value-of select="'Genres: '"/>
            <xsl:for-each select="genres/genre">
                <xsl:value-of select="."/>
                <xsl:text>, </xsl:text>
            </xsl:for-each>
            <xsl:text>&#10;</xsl:text>

            <xsl:value-of select="'Artists: '"/>
            <xsl:for-each select="artists/artist">
                <xsl:value-of select="."/>
                <xsl:text>, </xsl:text>
            </xsl:for-each>
            <xsl:text>&#10;</xsl:text>

            <xsl:value-of select="concat('Album Length: ', album_length)"/>
            <xsl:text>&#10;</xsl:text>

            <xsl:value-of select="concat('Release Date: ', release_date)"/>
            <xsl:text>&#10;</xsl:text>

            <xsl:value-of select="concat('Age Restriction: ', age_restriction)"/>
            <xsl:text>&#10;</xsl:text>

            <xsl:value-of select="'Tracks: '"/>
            <xsl:for-each select="tracks/track">
                <xsl:value-of select="concat(name, ' (', duration, ')')"/>
                <xsl:text>, </xsl:text>
            </xsl:for-each>
            <xsl:text>&#10;</xsl:text>

            <xsl:text>&#10;</xsl:text>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>
